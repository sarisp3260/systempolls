# SYSTEMAS DE ENCUESTAS

> Proyecto construido con python, postgres y django

## 💻 Pré-requisitos

Antes de comenzar, verifique que contienes los seguintes requisitos:
* Tener instalado python
* Visual Studio Code


##  Instalando

Para instalar el proyecto localmente, siga estas etapas:


<img src="https://img.shields.io/badge/Windows-017AD7?style=for-the-badge&logo=windows&logoColor=white" />

ingresa a tu ventana de comandos y ejecuta lo siguiente para clonar el repositorio
```
git clone https://github.com/diegoabt18/backtodolist.git
```
Instala las dependecias que se encuentra en el archivo requeriments.txt para eso inicia el entorno virtual de Python accedion con el siguiente comando
```
 .\env\Scripts\activate 
```
luego ejecuta el siguiente comando para instalar las dependencias
```
utiliza el comando "pip install requeriments.txt" 
```
Configura el archivo settings para añadir la conexion a la bases de datos de mongo db

settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT': {
            "host":"esrcibe aqui el nombre del host",
            "name":"nombre bases de datos",
            "authMechanism":"SCRAM-SHA-1" #For atlas cloud db
        },
    }
}
```

por utimo ejecuta el comando para iniciar el servidor localmente

```
py manage.py runserver
```

## ☕ Usando
<img  src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/>

<img  src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>

<img  src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white"/>

##  Capturas

![image](https://user-images.githubusercontent.com/47578861/166622754-9d9b2035-fea7-4761-bd0e-64d7198d0634.png)

![image](https://user-images.githubusercontent.com/47578861/166622810-a6d6521d-8575-4b34-8bc6-4d5679c2ccf2.png)



## 🤝 Autores


<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/Diegoabt18" width="100px;" alt="Foto do Diego Botello no GitHub"/><br>
        <sub>
          <b>Diego Botello</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
