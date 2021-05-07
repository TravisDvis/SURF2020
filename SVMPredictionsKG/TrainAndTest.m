%
% Time index of training/verification data needs to be in
% units of kyr for this code
%---------------------------------------------

clearvars 
close all
clc
Colors

load TrainingData.mat  

D=abs(D);
dt=t(2)-t(1);

%% Prediction horizon and window size

PH = 3.2;   % Prediction Horizon ***in kyr***
L = 20*dt;     % Size of data window ****in kyr*** 

SpecifyTrainingRatio = 'Y'; % "Y"-> Enforce P/N ratio in training data
PNratio = 100; % P/N ratio to enforce in training if SpecificyTrainingRatio = Y

PlotTraining = 'Y';       % Plot training
PlotVerification = 'N';   % Plot verification

WindowSize=round(L/dt);
DT=.1;    % Start-of-event threshold
RT=.8;    % End-of-event threshold


%% Label data

[Data,Labels]=GetLabeledData(t,D,DT,RT,PH,WindowSize);

%% Sort and train 

NP=sum(Labels==1);
NN=sum(Labels==0);

if SpecifyTrainingRatio=='Y'
    TrainingSizeP=NP;
    TrainingSizeN=min(NN,floor(TrainingSizeP*PNratio));
else
    TrainingSizeP=NP;
    TrainingSizeN=NN;
end
TrainingSize=TrainingSizeP+TrainingSizeN;

X=zeros(WindowSize,TrainingSize);

idx=find(Labels==0);
idx=idx(randperm(length(idx)));
X(:,1:TrainingSizeN)=Data(:,idx(1:TrainingSizeN));

idx=find(Labels==1);
idx=idx(randperm(length(idx)));
X(:,TrainingSizeN+1:end)=Data(:,idx(1:TrainingSizeP));
X=X.';
Labels=[zeros(TrainingSizeN,1);ones(TrainingSizeP,1)];

mdl = fitcsvm(X,Labels);

%% plot training
if PlotTraining == 'Y'
    if WindowSize>1
        figure
        subplot(121)
        plot(dt:dt:L,abs(X(1:TrainingSizeN,:)),'b')
        subplot(122)
        plot(dt:dt:L,abs(X(TrainingSizeN+1:end,:)),'b')
    else
        figure
        subplot(121)
        plot(dt:dt:L,abs(X(1:TrainingSizeN,:)),'b.')
        subplot(122)
        plot(dt:dt:L,abs(X(TrainingSizeN+1:end,:)),'b.')
    end
end


[MCC,ACC,~,P,N,~]=TestModel(t,abs(D),DT,RT,PH,WindowSize,mdl);
fprintf('Training\n')
fprintf('Positives (P):  %g\n',P)
fprintf('Negatives (N):  %g\n',N)
fprintf('ACC = %g\n',ACC)
fprintf('MCC = %g\n',MCC)
disp(' ')


%% Verification

load VerificationData.mat     

[MCC,ACC,Predictions,P,N,PN]=TestModel(t,abs(D),DT,RT,PH,WindowSize,mdl);

if PlotVerification=='Y'
    figure
    plot(t,D,'Color',Color(3,:),'LineWidth',2)
    hold on
    stairs(t(1+WindowSize-1:end),Predictions==1,'--','Color',Color(1,:),'LineWidth',2)
    stairs(t,PN==1,'Color',Color(2,:),'LineWidth',2)
    set(gca,'FontSize',16)
    box off
    legend('Dipole','Prediction','Truth')
    xlabel('Time')
end

fprintf('Verification\n')
fprintf('Positives (P):  %g\n',P)
fprintf('Negatives (N):  %g\n',N)
fprintf('ACC = %g\n',ACC)
fprintf('MCC = %g\n',MCC)

