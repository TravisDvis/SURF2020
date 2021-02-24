function reversal_times = getReversalTimes(xMatrix)
    reversal_times = double.empty(2,0);
    for kk = 1:(length(xMatrix)-1)
        if xMatrix(2,kk) >= 0
            sign = 0;
        else
            sign = 1;
        end
        if kk < length(xMatrix)+1
            if sign == 0 && xMatrix(2,kk+1) < 0
                time_index = [xMatrix(4,kk+1);xMatrix(5,kk+1)];
                fprintf('A dipole reversal has occurred at time: %i\n',xMatrix(4,kk+1));
                reversal_times = [reversal_times time_index];
            elseif sign == 1 && xMatrix(2,kk+1) >= 0
                time_index = [xMatrix(4,kk+1);xMatrix(5,kk+1)];
                fprintf("A dipole reversal has occurred at time: %i\n",xMatrix(4,kk+1));
                reversal_times = [reversal_times time_index];
            end
        end
    end
