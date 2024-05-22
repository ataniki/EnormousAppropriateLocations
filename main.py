def estimar_tempo_viagem(distância, velocidade_média): 
  tempo = distância/velocidade_média
  retorn tempo

distância =200
velocidade_media = 60
tempo_estimado =estimar_tempo_viagem(distância, velocidade_ media)
print ("para uma viagem de {}km e velocidade média de {} km, o tempo estimado é de {}". format ( distancia, velocidade_média, tempo_estimado))

