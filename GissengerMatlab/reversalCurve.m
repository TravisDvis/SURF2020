function reversal_curve = reversalCurve(xMatrix,threshold_pos,threshold_neg,reversal_times,dt)
    
    %Intialize reversal curve
    reversal_curve = zeros(1,length(xMatrix));
    crossed_reversed = crossAndReversed(xMatrix,threshold_pos,threshold_neg,reversal_times);

    width = uint16(0.5/dt);
    
    %Iterate through matrix/reversal times and indeces
    for i = 1:length(xMatrix)
        for ii = 1:size(crossed_reversed,1)
            for iii = 1:(length(crossed_reversed)-1)
                if i == crossed_reversed(ii,iii)
                    for iv = uint16(crossed_reversed(ii,iii)+1):uint16(crossed_reversed(ii,iii+1))
                       for v = 1:length(reversal_times)
                            if crossed_reversed(ii,iii) <= reversal_times(1,v) && crossed_reversed(ii,iii+1) >= reversal_times(1,v)
                                for vi = (uint16(reversal_times(1,v)+1)-width):uint16(reversal_times(1,v))
                                    reversal_curve(1,vi) = 1;
                                end
                                for vii = uint16(reversal_times(1,v)+1):uint16(crossed_reversed(ii,iii+1))
                                    reversal_curve(1,vii) = 2;
                                end
                            end
                       end
                    end
                end
            end
        end
    end
    