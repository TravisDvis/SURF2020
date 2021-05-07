function [MCC,ACC,Predictions,P,N,PN]=TestModel(t,D,DT,RT,PH,WindowSize,mdl)

[start,stop]=FindEvents(t,D,DT,RT);  
PN=PosNeg(t,start,stop,PH);

DataSize=length(PN)-WindowSize+1;
Predictions=zeros(1,DataSize);

TP=0;
FP=0;
TN=0;
FN=0;
P=0;
N=0;

for ii=1:DataSize
    Window=D(1+ii-1:WindowSize+ii-1).';
    
    if ismember(2,PN(1+ii-1:WindowSize+ii-1))
        Predictions(ii)=2;
    elseif ismember(1,PN(1+ii-1:WindowSize+ii-1))
        Predictions(ii)=predict(mdl,Window);
        P=P+1;
        if Predictions(ii)==1
            TP=TP+1;
        else
            FN=FN+1;
        end
    else
        Predictions(ii)=predict(mdl,Window);
        N=N+1;
        if Predictions(ii)==0
            TN=TN+1;
        else
            FP=FP+1;
        end
        
    end
end

ACC = (TP+TN)/(P+N);
MCC = (TP*TN - FP*FN) ...
        / sqrt( (TP+FP)*(TP+FN)*(TN+FP)*(TN+FN) );
    
