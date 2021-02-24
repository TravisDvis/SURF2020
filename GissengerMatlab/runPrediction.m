function skill_scores = runPrediction(xMatrix,threshold_pos,threshold_neg,reversal_times,dt)
    
    true_positive = 0;
    true_negative = 0;
    false_positive = 0;
    false_negative = 0;

    reversal_curve = reversalCurve(xMatrix,threshold_pos,threshold_neg,reversal_times,dt);
    
    for kk = 1:length(xMatrix)
        if xMatrix(2,kk) <= threshold_pos && xMatrix(2,kk) >= -1*threshold_neg
            reversal_prediction = true;
        else
            reversal_prediction = false;
        end
    %Compare prediction and reversal occurrences
        if reversal_prediction == true && reversal_curve(1,kk) == 1
            true_positive = true_positive + 1;
        elseif reversal_prediction == false && reversal_curve(1,kk) == 0
            true_negative = true_negative + 1;
        elseif reversal_prediction == true && reversal_curve(1,kk) == 0
            false_positive = false_positive + 1;
        elseif reversal_prediction == false && reversal_curve(1,kk) == 1
            false_negative = false_negative + 1;
        elseif reversal_curve(1,kk) == 2
            continue;
        end
    end
    
    fprintf('%i',false_negative);
    
    %Accuracy
    acc = (true_positive + true_negative)/(true_positive + true_negative + false_positive + false_negative);
    %F1 Score
    try
        f1 = (2*true_positive)/(2*true_positive + false_positive + false_negative);
    catch
        f1 = 0;
    end
    %Critical Success Index
    try
        csi = (true_positive)/(true_positive + false_positive + false_negative);
    catch
        csi = 0;
    end
    %Matthew's Correlation Coefficient
    mcc_num = ((true_positive*true_negative)-(false_positive*false_negative));
    mcc_den = sqrt((true_positive + false_positive)*(true_positive + false_negative)*(true_negative + false_positive)*(true_negative + false_negative));
    try
        mcc = mcc_num/mcc_den;
    catch
        mcc = 0;
    end
    %Storing all skill scores into an array
    skill_scores = [acc;f1;csi;mcc];
