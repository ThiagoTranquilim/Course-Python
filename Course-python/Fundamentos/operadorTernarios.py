esta_chovendo = True

print('hoje estou com a roupas ' + ('secas', 'molhadas')[esta_chovendo])

print('hoje estou com a roupas '+ ('molhadas'if(esta_chovendo == True) else('secas')))
