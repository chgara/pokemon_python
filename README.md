**Juego de Pokemon extensible:**<img src="/readme/p.gif" alt="Pokemon Game" width="500" height="303">

Un juego hecho con pygame en el que se puede cambiar todo sin tocar el código, solo hace falta editar los archivos de Json que se especifican más abajo. Para ejecutarlo &quot;python main.py&quot;.

**Descripción del proyecto:**

Es un juego retro al estilo pokemon. Su objetivo es una gran extensibilidad dando la posibilidad a la creación de mapas sin tener ni idea de programar. Los mapas, NPCs, pokemons, personas, estructuras pueden ser cambiados desde sus respectivos archivos sin tener que tocar nada de código. Además gracias a la arquitectura del juego sería muy fácil y limpio extenderlo y añadir las mecánicas de juego. Mostraré el juego en dos versiones, la versión &quot;normal&quot; y la versión de &quot;desarrollo&quot;.

- **Menú:**

  El menú del juego es muy simple. Se pueden crear nuevas partidas pulsando el botón &quot;+&quot; y acceder a otras ya guardadas clicando en ellas. (Las partidas se guardan con el comando CTRL+m). ![menu](https://i.ibb.co/tQ4Vbz7/menupokemon.png)

- **Guardado de partidas:**

  Las partidas por defecto se guardan en el directorio src/assets/saves/main.json. Se puede cambiar editando el archivo src/lib/configure.py y cambiando la constante &quot;SAVE_PATH&quot;. Nota importante: Si se cambiara el directorio hay que crear a mano el archivo json. Dentro de ese archivo el juego irá guardando cuando el jugador lo requiera pulsando CTRL+S.

- **Carga de mapas:**

  Por defecto el juego al crear una nueva partida carga el mapa tutorial. Pero a la hora de cargar una partida ya guardada lo que hará será cargar el archivo de guardado la dirección actual en memoria del mapa actual y cargará en el juego la posición del jugador más el mapa especificado en el juego. Además si al colisionar con una estructura está en su archivo de configuración especifica un mapa al que trasladarte el mapa actual cambiará.

- **Sistema de colisiones y su aplicaciones:**

  Al colisionar con una entidad del juego el jugador ejecuta una función específica que debe implementar la clase de esa entidad. Ahora mismo está implementado que las entidades de tipo NPC muestran un diálogo en la pantalla al colisionar con ellas. (El diálogo se deja de mostrar pulsando CTRL+C) y las entidades de tipo estructura cambian la escena del juego a la especificada, si no se especificara ninguna mandara al jugador al menú principal. Si quisiéramos extender podríamos crear una nueva clase que herede de entidad e implementar los métodos abstractos de la clase tal y como queramos.

**Arquitectura del software:**

Este juego consta de muchas clases por lo que un diagrama de UML completo rellenará 10 hojas de este PDF, con lo que me limitaré a mostrar una representación simple de como funciona el juego. Cabe destacarse que el juego a nivel de código esta muy bien documentado con lo que es fácil ir viendo como se ha montado la arquitectura, también es importante remarcar que para lograr la extensibilidad del código que voy a mostrar he usado numerosos patrones de diseño como el factory, strategy, observer,

decorator… en el código se referencian.

![arq](https://i.ibb.co/VJWYxRb/game.png)

**Como carga el juego los archivos:**

Su funcionamiento es simple pero ingenioso. Simplemente con poner en el código la dirección en memoria del primer mapa (por defecto el del tutorial) se puede cargar el juego entero. Porque editando el mapa del tutorial podemos especificar que lleve al jugador a otros distintos. Ahora voy a mostrar una representación simple de como funciona el juego, si se quiere ver en más detalle qué propiedades hay que especificar en el json se puede mirar en los mismos archivos.

![](https://i.ibb.co/86ffNFH/mapstructure.png)

Como se ve en la imagen al final es una estructura de nodos en la que un mapa tiene diferentes propiedades como: las entidades en las que solo se referencia su propio archivo para guardar la información de la misma; las estructuras que definen la propiedad map para llevarte a un nuevo mapa al colisionar con las mismas; esto crearía así una especie de grafo recursivo en el cual los mapas te llevan a más mapas y así infinitamente, solo limitado por la capacidad de uno mismo de crear mapas y entidades. A si que solo definiendo el mapa inicial se puede cargar el juego entero(ingenioso no? :).

- **Modo desarrollo:**

  <img src="/readme/d.gif" alt="My Project GIF" width="500" height="303">

  He añadido al juego la posibilidad de habilitar un modo &quot;desarrollo&quot; mediante el cual se muestran unas características especiales como mostrar las &quot;hitboxes&quot; de cada entidad, se muestra como se carga proceduralmente las entidades y el mapa, muestra en consola la posición del jugador y los fps ,si se la a la teclas &quot;i&quot; se para el juego y no se reanuda hasta que se de al enter en la consola

  (útil para &quot;debugar&#39;&#39;)...

  Este modo se puede activar simplemente editando el archivo src/lib/config.py editar la constante DEV_MODE = True.

  Cabe destacar que este modo consume muchos más recursos que el modo normal. Esto se debe a que en cada actualización del main game loop se carga el mapa entero de nuevo, esto es así para que si realizas algún cambio en el mapa que está el jugador se vea reflejado de inmediato sin necesidad de tener que abrir y cerrar el juego. Funciona de manera similar al &quot;Fast refresh&quot; que se utiliza en muchos frameworks de desarrollo web o de apps.
