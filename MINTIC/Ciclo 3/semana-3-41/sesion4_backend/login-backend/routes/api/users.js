const router = require('express').Router();
const userController = require('../../controllers/UserController.js');

//Ruta sería: /api/user/register (este es un método de registro)
router.post('/register', userController.register)

// Ruta sería: /api/user/listar
router.get('/listar', userController.listar)

//Ruta sería: /api/user/login (este es un método de logueo)
router.post('/login', userController.login)


module.exports = router;