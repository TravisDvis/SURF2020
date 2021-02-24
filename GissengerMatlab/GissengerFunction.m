function out = GissengerFunction(x)
Q = x(1);
D = x(2);
V = x(3);

m = 0.119;
nu = 0.1;
G = 0.9;

dQdt = m*Q-V*D;
dDdt = -nu*D+V*Q;
dVdt = G-V+Q*D;

out = [dQdt;dDdt;dVdt;0;0];