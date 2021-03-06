// Creamos un controlador y después los modelos
const {Sequelize, DataTypes} = require('sequelize');
const UserModel = require('./users');

// Conexión con base de datos
const sequelize = new Sequelize('CxVs7Qhuxr', 'CxVs7Qhuxr', 'KaxGSCwQ0J', {
    host: 'remotemysql.com',
    port: '3306',
    dialect: 'mysql',
  });

// Nos traemos el modelo creado
const User = UserModel(sequelize,Sequelize);

// Sincronizamos la base de datos
sequelize.sync({ force: false })
  .then(()=>{
    console.log('Tablas sincronizadas')
  })

  // Exportamos el modelo para poder utilizarlo
  module.exports= {
    User
  }