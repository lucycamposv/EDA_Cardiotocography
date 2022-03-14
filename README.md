# EDA_Cardiotocography

EDA - Bootcamp The Bridge

**Introducción:**

La cardiotocografía (CTG) es un método de evaluación fetal que registra simultáneamente la frecuencia cardiaca, los movimientos fetales y las contracciones uterinas. Se utiliza comúnmente en el tercer trimestre y su propósito es monitorear el bienestar fetal. Estas mediciones ayudan a los profesionales de la salud a verificar el estado general del feto y a identificar las primeras señales de sufrimiento fetal. Sin embargo, se producen muchos falsos positivos, por lo que encontrar una relación causal podría permitir mejorar la clasificación de la salud fetal.

**Objetivo:**

Este proyecto pretende analizar registros cardiotocográficos fetales para estudiar la relación entre características de la CTG y la evaluación del estado fetal.

Hipótesis principal:
> Existe una relación causal entre las características de la CTG y los estados de salud fetal.

Hipótesis secundarias:
> La aceleración de la frecuencia cardiaca fetal tiene una correlación negativa con la mortalidad fetal.
> 
> La frecuencia cardiaca basal fuera del rango 110-160 lpm indica sufrimiento fetal.

**Metodología**:

Datasets extraídos de kaggle:
* [Fetal Health Classification](https://www.kaggle.com/andrewmvd/fetal-health-classification)
* [Fetal Cardiotocography Data](https://www.kaggle.com/akshat0007/fetalhr)

**Conclusiones:**
1. Aceleraciones, Desaceleraciones y Variabilidad afectan directamente al estado de salud fetal. Las aceleraciones son las variables más importantes.
2. La frecuencia cardiaca fetal no es indicativo de un pronóstico patológico.
3. Contracciones uterinas afectan de forma indirecta, están relacionadas con las desaceleraciones.
4. Aumento en las aceleraciones incrementa la probabilidad de índice Normal. En cambio, aumento de desaceleraciones y variabilidad aumentan la probabilidad de índice Patológico.
