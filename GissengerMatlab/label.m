function label = label(xMatrix,pos_threshold,neg_threshold)
    
    L = 8;
    label = zeros(length(xMatrix)-(L-1),L);
    
    for kk1 = 1:(length(xMatrix))
       
        for kk2 = kk1:(length(xMatrix))
            
            for kk3 = kk2:kk2+(size(label,2))-1
                %If the index is equal to the last of the xMatrix, exit and return the labels
                if kk3 == length(xMatrix)
                    return
                end
                %If this is the first index in the label
                if kk3==kk2
                    %If a reversal already occurred, ignore
                    if xMatrix(2,kk3) < pos_threshold && xMatrix(2,kk3) > neg_threshold 
                        label(kk2,kk3-kk2+1) = 2;
                        continue
                    end
                end
                %If this is NOT the first index in the label
                if kk3>kk2
                    %If the previous index indicated a reversal or ignore, ignore
                    if label(kk2,kk3-kk2) == 1 || label(kk2,kk3-kk2) == 2
                        if xMatrix(2,kk3) < pos_threshold && xMatrix(2,kk3) > neg_threshold 
                            label(kk2,kk3-kk2+1) = 2;
                            continue
                        end 
                    end
                    %If the xMatrix value is within the threshold range, indicate a reversal
                    if xMatrix(2,kk3) < pos_threshold && xMatrix(2,kk3) > neg_threshold 
                        label(kk2,kk3-kk2+1) = 1;
                    end
                    
                end
                
            end
            
        end
        
    end
