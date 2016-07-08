Title: Como copiar vídeos de qualquer site e em qualquer formato para o seu computador
Date: 2011-12-21 20:07
Author: admin
Category: hacking, software.livre, tech, tutoriais, vídeo
Tags: firefox, gnulinux, tutorial, vídeo
Slug: como-salvar-videos-de-qualquer-site-e-em-qualquer-formato-para-o-seu-computador
Status: published

Há muito tempo, postei [aqui no
blog](http://wille.blog.br/2008/05/a-forma-mais-facil-de-baixar-videos-do-you-tube/ "a forma mais fácil de baixar vídeos do You Tube")
uma forma bem fácil de copiar vídeos do youtube no GNU/Linux. Bastava
esperar o vídeo carregar no navegador e ir lá no /tmp/ e copiar o
arquivo pra outra pasta. Eu usava bastante isso. Porém com uma mudança
no plugin do Adobe Flash e com o uso de
[HTML5](http://pt.wikipedia.org/wiki/HTML5) no [You
Tube](www.youtube.com/html5), essa técnica passou a não funcionar mais.

Há uns meses, [Liquuid postou em seu
blog](http://blog.liquuid.net/2011/03/26/como-salvar-um-video-do-youtube-no-novo-flash-plugin/)
como copiar vídeos carregados com o novo plugin Flash, porém descobri
uma forma mais fácil e rápida e que funciona também com vídeos em sites
que já estão utilizando HTML5.

Primeiro espere o vídeo ser carregado totalmente no
[Firefox](http://getfirefox.com/) (creio que essas instruções funcionam
em outros navegadores também, desde que rodando no GNU/Linux). Quando
finalizar o carregamento, execute o comando:

`ps aux | grep firefox`

O resultado será algo parecido com isso:

`wille     1366  9.7 17.9 1511896 547344 ?      Sl   17:42  13:17 firefox wille     1444  3.8  2.9 592744 90248 ?        Sl   17:42   5:16 /usr/lib/firefox/plugin-container /usr/lib/mozilla/plugins/libflashplayer.so -greomni /usr/lib/firefox/omni.jar 1366 plugin wille     2648  0.0  0.0   8576  1016 pts/0    S+   19:58   0:00 grep firefox`

Preste atenção nos números em negrito. São os números de processo do
firefox e do plugin flashplayer, respectivamente.  Daí, basta abrir o
diretório **/proc/1366/fd/** ou o **/proc/1444/fd/** no Gerenciador de
Arquivos e, pelo ícone do arquivo, é possível identificar qual é o
arquivo do vídeo que está carregado no Firefox. Uma dica: se o vídeo foi
carregado com HTML5, geralmente ele está no diretório do processo do
firefox, se foi carregado com flashplayer, tá no outro.

![nautilus abrindo o diretório citado
acima](http://images.wille.blog.br/nautilus.jpg "observe o ícone diferente no nautilus")

Porém, não dá pra usar o Nautilus para copiar, pois esse arquivo que
aparece na tela é apenas um link para um outro arquivo que já foi
deletado, assim utilize o terminal para fazer a cópia (quem não sabe
copiar pelo terminal, estude o comando **cp**).

É bom lembrar que esse tutorial é válido para qualquer site de vídeo,
não apenas o You Tube.

**UPDATE:** Pra identificar o vídeo, é possível também usar o terminal.
Basta executar o comando **ls -lah** nos diretórios citados acima. No
caso de sites que usem Flash, é só observar qual o link que aponta para
**/tmp/Flashxxxx**.

**UPDATE 2:** Com o Flash 11, essa dica não funciona mais. A solução que
encontrei foi usar um plugin no Firefox chamado [Flash Video
Downloader](http://www.flashvideodownloader.org).
