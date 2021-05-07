%
% Time index of training/verification data needs to be in
% units of kyr for this code
%---------------------------------------------

clear 
close all
clc
Colors

load TrainingData.mat  
D=abs(D);
dt=t(2)-t(1);
DT=.1;    % Start-of-event threshold
RT=.8;    % End-of-event threshold

%% Prediction horizon and window size
PH = 3.2;       % Prediction Horizon ***in kyr***
%L  = 1*dt;     % Size of data window ****in kyr*** 

WindowSize = [1 10 50 100 150 200];
MCC_WindowSize = zeros(length(WindowSize),1);

MCCWs = zeros(length(WindowSize),1);
OWs = zeros(length(WindowSize),1);
OMs = cell(length(WindowSize),1);
OTSs = zeros(length(WindowSize),1);


%Checkpoint
for i = 1:length(WindowSize)
    %% Label data
    [Data,Labels]=GetLabeledData(t,D,DT,RT,PH,WindowSize(i));

    %% Sort and train 
    
    %Random Undersampling
    
    NP=sum(Labels==1);
    NN=sum(Labels==0);
    
    TrainingSizeN = [30000 35000 40000 45000 NN];
    
    TrainingSizeP=NP;
    
    idx0=find(Labels==0);
    idx1=find(Labels==1);
    
    for j = 1:length(TrainingSizeN)
        
        
        TrainingSize = TrainingSizeN(j) + TrainingSizeP;
        X=zeros(WindowSize(i),TrainingSize);
        
        idx0_temp=idx0(randperm(length(idx0),TrainingSizeN(j)));
        X(:,1:TrainingSizeN(j))=Data(:,idx0_temp(1:TrainingSizeN(j)));
        
        idx1_temp=idx1(randperm(length(idx1)));
        X(:,TrainingSizeN(j)+1:end)=Data(:,idx1_temp(1:TrainingSizeP));
    
        X=X.';
        Labels=[zeros(TrainingSizeN(j),1);ones(TrainingSizeP,1)];
        
    
        fprintf('Training data\n')
        fprintf('Positives (P):  %g\n',NP)
        fprintf('Negatives (N):  %g\n',NN)
        disp(' ')

        %% optimize weight using the MCC
        cij = .1:.1:1;
        MCCSave = zeros(length(cij),1);
        optMCC = 0;
        optWeight = 0;

        for kk=1:length(cij)
            fprintf('Tuning step %g/%g\n',kk,length(cij))
            mdl = fitcsvm(X,Labels,'Cost',[0 cij(kk);1 0]);
            [MCC,ACC,~,~,~,~]=TestModel(t,abs(D),DT,RT,PH,WindowSize(i),mdl);
    
            MCCSave(kk) = MCC;
            if MCC>optMCC
                optMCC = MCC;
                optModel = mdl;
                optWeight = cij(kk);
            end
            fprintf('Window Size = %g\n',WindowSize(i))
            fprintf('ACC = %g\n',ACC)
            fprintf('MCC = %g\n',MCC)
            fprintf('Training Size (N) = %g\n',TrainingSizeN(j));
            fprintf('Current optimal MCC: %g\n',optMCC)
            disp(' ')
        end
        
        if optMCC>MCCWs(i)
            MCCWs(i) = optMCC;
            OWs(i) = optWeight;
            OMs{i} = optModel;
            OTSs(i) = TrainingSizeN(j);
        end
        
    end
    
end

[optMCC,optMCCIndex] = max(MCCWs);

optWindowSize = WindowSize(optMCCIndex);
optWeight = OWs(optMCCIndex);
optTrainingSizeN = OTSs(optMCCIndex);

disp(' ')
fprintf('Best model window size: %g\n',optWindowSize)
fprintf('Best model weight: %g\n',optWeight)
fprintf('Best model MCC: %g\n',optMCC)
fprintf('Best model TrainingSize (N): %g\n',optTrainingSizeN)
disp(' ')

figure
plot(WindowSize,MCCWs,'Color',[0,0.7,0.9])
title('Training Data Window Sizes vs. Optimal MCC Values')
xlabel('Window Size')
ylabel('Optimal MCC')

%% verification of best model

MCCWsVD = zeros(length(WindowSize),1);

for i = 1:length(WindowSize)
    
    load VerificationData.mat     

    [MCC,ACC,Predictions,P,N,PN]=TestModel(t,abs(D),DT,RT,PH,WindowSize(i),OMs{i});
    
    disp(' ')
    fprintf('Verification\n')
    fprintf('Positives (P):  %g\n',P)
    fprintf('Negatives (N):  %g\n',N)
    fprintf('ACC = %g\n',ACC)
    fprintf('MCC = %g\n',MCC)
    disp(' ')
    
    MCCWsVD(i) = MCC;

end

figure
plot(WindowSize,MCCWsVD,'Color',[0,0.7,0.9])
title('Verification Data Window Sizes vs. Optimal MCC Values')
xlabel('Window Size')
ylabel('Optimal MCC')


