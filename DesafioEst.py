#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importando módulo da lib para arquivos Portable Executable(PE).
import pefile

# Passando o arquivo executavel para a function e armazenando-o na variável
pe = pefile.PE("/root/Desktop/A/W10ATTEXES/cmd.exe")

# Exibindo dados contidos no executavel
pe.print_info()


# Referências:
# https://axcheron.github.io/pe-format-manipulation-with-pefile/
# https://pypi.org/project/pefile/
# https://bufferoverflows.net/exploring-pe-files-with-python/

# Nota: O processo de depuração pode ser feito de algumas formas e consiste em entender
# A estrutura de execução do software.
# Em sistemas linux gosto de usar o "GDB", em sistemas Windows uso o "Immunity Debugger"
# A engenharia reversa de software é uma técnica usada para muitos fins
# Entretanto o mais crítico deles é a manipulação da stack que controla o fluxo
# De execução de um software, um usuário mal intencionado pode injetar códigos
# E pôr em risco a integridade, confidencialidade ou a disponibilidade da aplicação.

# Github do autor @BlackCyber21.
