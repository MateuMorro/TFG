function nousPunts=remuestreo(point,w,genetico)

  if genetico==1
    maxim=0;
    cont=0;
    for i=1:length(w)
      if maxim<w(i)
        maxim=w(i);
        cont=i;
      end
    end

    ones(1,length(w)).*point(cont);
    ones(1,length(w)).*[2*rand(1,length(w))-1].*4;
    nousPunts=ones(1,length(w)).*point(cont)+ones(1,length(w)).*[2*rand(1,length(w))-1].*6;
    
  else
    point;
    w;
    sumaAbsoluta=zeros(1,length(w)+1);
    x=cumsum(w);
    for i=1:length(x)
      sumaAbsoluta(i+1)=x(i);
    end
    sumaAbsoluta;
    #v=linspace(0.000001,0.999999,length(w)+2);
    v=rand(1,length(w));

    
    contador=zeros(length(w),length(w));
  

    for j=1:length(w)
      for i=1:length(w)
        if v(j)>=sumaAbsoluta(i) && sumaAbsoluta(i+1)>v(j) 
          v(j);
          sumaAbsoluta(i);
          contador(j,i)=contador(j,i)+1;
        end
      end
    end
    contador;
    h=zeros(1,length(w));
    for i=1:length(w)
      h(i)=sum(contador(: ,i));
    end
    h;
    
    nousPunts=ones(1,length(w));

    k=1;
    for i=1:length(h)
      for j=1:h(i)
        g=point(i)+(2*rand(1,1)-1)*5;
        g=max(0,g);
        g=min(100,g);
        nousPunts(k)=g;
        k=k+1;
      end
    end
    nousPunts;
    
  end  
  