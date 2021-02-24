function crossed_threshold = crossThreshold(xMatrix,threshold_pos,threshold_neg)
        
    crossed_threshold = double.empty(2,0);
    crossed_threshold_1 = [];

    count = 0;

    for kk = 1:(length(xMatrix)-1)
        
        if xMatrix(2,kk) > threshold_pos
            sign_before = 0;
        elseif xMatrix(2,kk) < -1*threshold_neg
            sign_before = 1;
        elseif xMatrix(2,kk) <= threshold_pos && xMatrix(1,kk) >= -1*threshold_neg
            sign_before = 2;
        end

        if xMatrix(2,kk+1) > threshold_pos
            sign_after = 3;
        elseif xMatrix(2,kk+1) < -1*threshold_neg
            sign_after = 4;
        elseif xMatrix(2,kk+1) <= threshold_pos && xMatrix(1,kk+1) >= -1*threshold_neg
            sign_after = 5;
        end

        if sign_before == 0 && (sign_after == 4 || sign_after == 5)
            crossed_threshold_1 = [crossed_threshold_1 kk+1];
            count = count + 1;
        elseif sign_before == 1 && (sign_after == 3 || sign_after == 5)
            crossed_threshold_1 = [crossed_threshold_1 kk+1];
            count = count + 1;
        elseif sign_before == 2 && (sign_after == 3 || sign_after == 4)
            crossed_threshold_1 = [crossed_threshold_1 kk+1];
            count = count + 1;
        end

        if count == 2
            count = 0;
            crossed_threshold = [crossed_threshold crossed_threshold_1];
            crossed_threshold_1 = [];
        end
    end    

end