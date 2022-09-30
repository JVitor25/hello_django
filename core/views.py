from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos!</h1>'. format(nome, idade))

def soma(request, numA, numB):
    soma = numA + numB
    return HttpResponse('<h1>A soma é: {}!</h1>'.format(soma))

def subtracao(request, numA, numB):
    subtracao = numA - numB
    return HttpResponse('<h1>A subtração é: {}!</h1>'.format(subtracao))

def multiplicacao(request, numA, numB):
    multiplicacao = numA * numB
    return HttpResponse('<h1>A multiplicação é: {}!</h1>'.format(multiplicacao))

def divisao(request, numA, numB):
    divisao = numA / numB
    return HttpResponse('<h1>A divisão é: {}!</h1>'.format(divisao))