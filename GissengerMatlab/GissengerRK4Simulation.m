%%
clear 
close all
clc

dt = 0.1;

T = 100;
nSteps = T/dt;
xo = [1;2;3;0;1];
x = RK4Scheme(xo,dt,nSteps);
xo = x(:,end);

T = 1000;
t = 0:dt:T;
nSteps = T/dt;
x = RK4Scheme(xo,dt,nSteps);

figure
subplot(311), plot(t,x(1,:))
subplot(312), plot(t,x(2,:))
subplot(313), plot(t,x(3,:))

figure
plot3(x(1,:),x(2,:),x(3,:))

figure
for kk=1:nSteps
    if mod(kk,10)==0
        plot3(x(1,1:kk),x(2,1:kk),x(3,1:kk),'-','LineWidth',1)
        hold on,plot3(x(1,kk),x(2,kk),x(3,kk),'.','Color','r','MarkerSize',20)
        axis([-2.5 2.5 -2.5 2.5 -2.5 2.5])
        view([90 0])
        drawnow
        hold off
    end
end
reversal_times = getReversalTimes(x);
skillSweep(x,reversal_times,dt);