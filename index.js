const express = require("express")
const app = express()
const port = 3000

app.get('/ola', (req, res)=>{
    res.send("Hello Class!")
})

app.get('/serie', (req, res)=>{
    const serie = require("./Serie.json")
    res.json({resposta: serie})
})

app.listen(port, ()=>{
    console.log("API executando na porta" + port)
})
