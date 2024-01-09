<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Shell Simples em Python</h1>

<p>Este é um shell simples implementado em Python que permite a execução de comandos, acompanhados de algumas funcionalidades adicionais. O shell suporta a execução concorrente de comandos, mantém um histórico das últimas 10 entradas e oferece a capacidade de visualizar os IDs do processo pai e filho.</p>

<h2>Funcionalidades</h2>

<ol>
    <li><strong>Execução de Comandos:</strong> O shell pode executar comandos fornecidos pelo usuário. A execução pode ser feita de forma sequencial ou concorrente, dependendo da presença do caractere '&' no final do comando.</li>
    <li><strong>Visualização de IDs de Processo:</strong> O shell exibe os IDs do processo pai e filho durante a execução dos comandos.</li>
    <li><strong>Histórico de Comandos:</strong> Mantém um histórico das últimas 10 entradas, acessível através do comando "history".</li>
</ol>

<h2>Uso</h2>

<ol>
    <li>Execute o script Python</li>
    <li>Digite os comandos desejados no prompt "osh>". Utilize "&" no final do comando para executá-lo de forma concorrente.</li>
    <li>Explore as funcionalidades do shell, incluindo a visualização de IDs de processo e o histórico de comandos.</li>
</ol>

<h2>Exemplos</h2>

<code>osh> ls</code>
<p>Executa o comando 'ls' de forma sequencial.</p>

<code>osh> sleep 5 &</code>
<p>Executa o comando 'sleep 5' de forma concorrente.</p>

<code>osh> history</code>
<p>Exibe os últimos 10 comandos inseridos.</p>

<h2>Contribuição</h2>

<p>Contribuições são bem-vindas! Sinta-se à vontade para propor melhorias, relatar problemas ou enviar pull requests para este projeto.</p>

</body>
</html>
