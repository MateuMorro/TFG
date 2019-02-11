n=20;
t=linspace(0,2*pi,80);
v_x_circum=50+30*cos(t);
v_y_circum=50+30*sin(t);

bolla_x_0=v_x_circum(1);
bolla_y_0=v_y_circum(2);

inici_x=ones(1,n).*rand(1,n)*100;
length(inici_x);
inici_y=ones(1,n).*rand(1,n)*100;

name = sprintf('Imatge_genetica_%d.jpg ',1);
plot(bolla_x_0,bolla_y_0,'o-r',inici_x,inici_y,'*b');
figure(1);
print('-djpeg','-r150',name);


for i=1:75
prediccio_x=DistanciaParticulesABolla(bolla_x_0,inici_x);
prediccio_y=DistanciaParticulesABolla(bolla_y_0,inici_y);

bolla_x_1=v_x_circum(i+1);
bolla_y_1=v_y_circum(i+1);

w_x=(100-prediccio_x)./sum(100-prediccio_x);
w_y=(100-prediccio_y)./sum(100-prediccio_y);
nou_x=remostreig(inici_x,w_x,1);
nou_y=remostreig(inici_y,w_y,1);

name = sprintf('Imatge_genetica_%d.jpg ',i+1);
plot(bolla_x_1,bolla_y_1,'o-r',nou_x,nou_y,'*b');
axis([0 100 0 100])
figure(1);
print('-djpeg','-r150',name);



bolla_x_0=bolla_x_1;
bolla_y_0=bolla_y_1;
inici_x=nou_x;
inici_y=nou_y;
end