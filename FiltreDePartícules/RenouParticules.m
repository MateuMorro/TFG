function particules=RenouParticules(part,maximEnfora,minimEnfora)  
  particules=part+ones(1,length(part)).*[2*rand(1,length(part))-1].*7;
  particules=min(maximEnfora,particules);
  particules=max(minimEnfora,particules);
end
    