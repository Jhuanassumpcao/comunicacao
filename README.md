## RZ UNIPOLAR

### Lei de formação: 
Para cada bit "1" na sequência de dados a ser transmitida, um pulso com nível lógico alto é transmitido durante um determinado período de tempo, enquanto para cada bit "0", não há transmissão de sinal (ou seja, o sinal permanece em nível baixo) durante o mesmo período de tempo. Ao final do período de tempo, o sinal retorna ao nível zero.

### Sincronismo: 
Não possui um sinal de sincronismo específico. Em geral, o sincronismo é obtido por meio de outros mecanismos, como o uso de um relógio (clock) para sincronizar a transmissão e a recepção dos dados, ou através do uso de técnicas de codificação de linha que incluem bits adicionais de sincronismo ou controle de erro.

### Componente DC:
Não possui um componente DC, ou seja, não apresenta um nível de corrente contínua (DC) constante. Isso ocorre porque, durante a transmissão de cada bit, o sinal oscila entre níveis positivos (para bits "1") e zero (para bits "0"), retornando sempre ao zero antes do próximo bit ser transmitido.

### Imunidade a ruídos: 
Apresenta uma imunidade limitada a ruídos, ou seja, a presença de interferências eletromagnéticas ou outros tipos de ruído na linha de transmissão pode afetar a qualidade da comunicação e levar a erros de transmissão. Pois, ele transmite informações apenas através da presença ou ausência de pulsos de sinal, o que pode torná-lo mais suscetível a ruídos e distorções.

### Aplicação prática:
 Padrão IEEE 802.3


## RZ BIPOLAR

### Lei de formação: 
Nessa técnica, um bit 1 é representado por uma transição do sinal no meio do bit, seguida por um retorno à linha de base positiva, enquanto que um bit 0 é representado por uma transição do sinal no meio do bit, seguida por um retorno à linha de base negativa.

### Sincronismo: 
Sincronismo por tempo e o sincronismo por codificação.

No sincronismo por tempo, o transmissor e o receptor são sincronizados por um sinal de clock comum que é enviado juntamente com os dados. Cada bit é transmitido em um período de clock específico, o que permite ao receptor identificar o início e o fim de cada bit e reconstruir a palavra de dados original.

No sincronismo por codificação, um ou mais bits especiais são adicionados à palavra de dados para indicar o início e o fim da transmissão, bem como para identificar cada bit individualmente. Esses bits são chamados de bits de sincronismo e são reconhecidos pelo receptor para sincronizar e reconstruir a palavra de dados original.

### Componente DC:
É o valor médio do sinal de transmissão, ou seja, a componente de frequência zero do sinal. Como o código de linha RZ bipolar utiliza níveis de tensão positivos e negativos para representar os bits, o componente DC é tipicamente zero, já que as polaridades positiva e negativa são equilibradas.

### Imunidade a ruídos: 
Quando um sinal é transmitido utilizando o código, o ruído introduzido no canal de comunicação afeta tanto a polaridade positiva quanto a negativa dos níveis de tensão, o que pode reduzir o nível de ruído total. Além disso, o sinal pode ser recuperado mais facilmente pelo receptor, já que a presença de ambas as polaridades positiva e negativa ajuda a distinguir os bits individuais e a reconstruir a palavra de dados original.

### Aplicação prática:
  Ethernet 100Base-TX.
  RS-232 e RS-485.
