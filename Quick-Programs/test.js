const express = require('express');

const app = express();

app.get('/api/users', (req,res) => {
  res.send('My User');
});

const PORT = process.env.PORT || 8000;

app.listen(PORT, () => console.log(`Server Running On Port PORT`));