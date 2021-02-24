function skillSweep(xMatrix,reversal_times,dt)

    threshold_vector = double.empty(3,0);
    sweep_parameter = 50;

    for i = 1:sweep_parameter
        for j = 1:sweep_parameter
            sweep = runPrediction(xMatrix,i/sweep_parameter,j/sweep_parameter,reversal_times,dt);
            slabel = label(xMatrix,i/sweep_parameter,j/sweep_parameter);
            mcc = sweep(4,1);
            if mcc == 0
                continue;
            end
            current_threshold = [i/sweep_parameter;j/sweep_parameter;mcc];
            threshold_vector = [threshold_vector current_threshold];
        end
    end
    %Find column index where max MCC occurs
    [row,column] = find(threshold_vector(3,:) == max(threshold_vector(3,:)));
    %Indicate optimal threshold
    optimal_threshold_pos = threshold_vector(1,column);
    optimal_threshold_neg = threshold_vector(2,column);
    fprintf("The optimal positive threshold(s) is/are: %i",optimal_threshold_pos);
    fprintf(", and the optimal negative threshold(s) is/are: %i",optimal_threshold_neg);
    fprintf(" with an MCC of: %i", max(threshold_vector(3,:)));
    %Plot Threshold values vs MCC
    figure
    for kk = 1:length(threshold_vector)
        if mod(kk,10)==0
            plot3(threshold_vector(1,1:kk),threshold_vector(2,1:kk),threshold_vector(3,1:kk),'-','LineWidth',1)
            hold on,plot3(threshold_vector(1,kk),threshold_vector(2,kk),threshold_vector(3,kk),'.','Color','r','MarkerSize',20)
            axis([-2.5 2.5 -2.5 2.5 -2.5 2.5])
            view([90 0])
            drawnow
            hold off
        end
    end
    
