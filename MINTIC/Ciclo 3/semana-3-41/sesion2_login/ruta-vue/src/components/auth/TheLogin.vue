<template>
<div class="container mt-5">
  <form>
    <div class="form-group">

      <label for="exampleInputEmail1">Email address</label>

      <input
        v-model="login.email"
        type="email"
        class="form-control"
        id="exampleInputEmail1"
        aria-describedby="emailHelp"
        placeholder="Enter email"
      />

      <small id="emailHelp" class="form-text text-muted"
        >We'll never share your email with anyone else.</small>
    </div>

    <div class="form-group">
      <label for="exampleInputPassword1">Password</label>
      <input
        v-model="login.password"
        type="password"
        class="form-control"
        id="exampleInputPassword1"
        placeholder="Password"
      />
    </div>

    <button 
    @click.prevent="loginUser"
    type="submit" 
    class="btn btn-primary">Submit</button>

    <pre>
        {{login}}
    </pre>

  </form>
</div>
</template>

<script>
import swal from 'sweetalert';
export default {
    name: 'TheLogin',
    data(){
        return {
            login:{
                email:'',
                password:'',
            }
        }
    },
    methods: {
        async loginUser(){
            try {
                let response = await this.$http.post('/api/user/login', this.login);
                console.log(response.data)
                let token = response.data.tokenReturn;
                let user = response.data.user;

                localStorage.setItem('jwt', token);
                localStorage.setItem('user', JSON.stringify(user));
                if(token){
                    swal("Éxito!", "Login correcto", "success");
                    this.$router.push('/home');
                }
            } catch (e) {
                swal("Oops!", "Algo salió mal", "error");
                // console.log(err.response);
            }
        }
    }
}
</script>