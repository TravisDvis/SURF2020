function xMatrix = RK4Scheme(xo,dt,nSteps)
    %Set initial vector
    x = xo;
    xMatrix = xo;
    %Initialize time
    t = 0;
    for kk = 1:nSteps
        %Increment time
        t = t + dt;
        %Set k values
        k1 = GissengerFunction(x);
        k2 = GissengerFunction(x + 0.5*dt*k1);
        k3 = GissengerFunction(x + 0.5*dt*k2);
        k4 = GissengerFunction(x +     dt*k3);
        %Update x vector
        index_vector = [0;0;0;dt;1];
        x = x + (dt/6)*(k1+2*k2+2*k3+k4) + index_vector;
        %Append current x vector to the x matrix
        xMatrix = [xMatrix x];
    end
    