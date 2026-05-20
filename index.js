const express = require("express")
const app = express()
const port = 3002

app.get('/olá', (req, res)=>{
    res.send("Hello Class!")
})

app.listen(port, ()=>{
    console.log("API executando na porta" + port)
})