function crossed_and_reversed = crossAndReversed(xMatrix,threshold_pos,threshold_neg,reversal_times)
    
    crossed_threshold = crossThreshold(xMatrix,threshold_pos,threshold_neg);
    crossed_and_reversed = double.empty(2,0);
   
    for i = 1:size(crossed_threshold,1)
        for ii = 1:(length(crossed_threshold)-1)
            for iii = 1:length(reversal_times)
                if reversal_times(2,iii) >= crossed_threshold(i,ii) && reversal_times(2,iii) <= crossed_threshold(i,ii+1)
                    crossed_and_reversed_1 = [crossed_threshold(i,ii),crossed_threshold(i,ii+1)];
                    crossed_and_reversed = [crossed_and_reversed crossed_and_reversed_1];
                end
            end
        end
    end
    
 