function clicou(){
          let nome = String(window.prompt('Qual é o nome do aluno?'))
          
          let nota1 = Number(window
          .prompt(`Primeira nota de ${nome}`))
          
          let nota2 = Number(window
          .prompt(`Segunda nota de ${nome}`))
          
          let m = (nota1+nota2)/2
          
          res.innerHTML = `<h2><strong>Analisando a situação de ${nome}</strong></h2>`
          
          res.innerHTML += `Com as notas de ${nota1} e ${nota2} a <strong>média é de ${m}<br></strong>`
          
          if (m > 6){
              res.innerHTML += `Com a média acima 6,0, o aluno está <strong><span class='ap'>APROVADO</span></strong>`
          }else if (m >= 3){
              res.innerHTML += `Com a média entre 3,0 e 6,0, o aluno está em <strong><span class='re'>RECUPERAÇÃO</span></strong> `
          }else {
              res.innerHTML += `Com a média abaixo 3,0, o aluno está <strong><span class='rep'>REPROVADO</span></strong> `
          }
}
        
        
