//declarando variaveis
programa {
  funcao inicio() {

    inteiro num1, num2

    escreva("\nDigite um numero qualquer: ") 
    leia(num1)
    escreva("\nDigite outro numero qualquer: ")
    leia(num2)

    real soma
    soma = num1 + num2

   // concatenação -> ( "+" e ",")

    escreva("\n O resultado de ", num1, " + " , num2, " é: ", soma)
    escreva("\n O resultado é: " , soma, "\n")

    escreva("\n Pula a linha\n")

    real sub, multi, div, modulo
    sub = num1 - num2
    multi = num1 * num2
    div = num1 / num2
    modulo = num1 % num2

    escreva("\n Resultado da subtração: ",sub)
    escreva("\n Resultado da multiplicação: ",multi)
    escreva("\n Resultado da divisão: ",div)
    escreva("\n Resultado do resto da divisão: ",modulo)

    //////////////////////////////////////////////////////////

    /* Operadores Aritiméticos

    +  -> SOMA
    -  -> SUBTRAÇÃO
    /  -> DIVISAO COMUM
    // -> DIVISÃO INTEIRA
    *  -> MULTIPLICAÇÃO
    ** -> EXPONENCIAÇÃO
    %  -> MODULO DE DIVISÃO

    */ //////////////////////////////////////////////////////

    /*Operadores de Comparação

    >= : MAIOR IGUAL
    <= : MENOR IGUAL
    != : DIFERENTE
    == : IGUAL
    >  : MAIOR
    <  : MENOR

    */ //////////////////////////////////////////////////////

    /* Operadores de Atribuição

    =  : ATRIBUIÇÃO DE VALOR
    += : INCREMENTA
    -= : DECREMENTA
    *= : MULTIPLICA PELO VALOR
    /= : DIVIDE PELO VALOR

    */ //////////////////////////////////////////////////////

    /* Operadores Lógicos
    
    AND : Faz o papel do conectivo "E" (as duas preposições precisam ser verdadeiras para o resultado ser verdadeiro)
    &&

    OR  : Faz o papel do conectivo "OU" (uma ou outra preposição precisa ser verdadeira para o resultado ser verdadeiro)
    ||

    NOT : Faz o paepl do conectivo "NÃO" (onde ele irá negar uma preposição)
    !

    */

   // fim da linha

    

    
  }
}
