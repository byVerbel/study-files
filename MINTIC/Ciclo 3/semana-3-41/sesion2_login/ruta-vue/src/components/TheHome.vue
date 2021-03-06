<template>
<div>

  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Página</a>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <form class="form-inline my-2 my-lg-0">
        <button 
        class="btn btn-outline-success my-2 my-sm-0" 
        type="button"
        @click="logOut">
          Logout
        </button>
      </form>
    </div>
  </nav>

  <div class="container">
      <p>
          {{user.name}}
      </p>
      <p>
          {{user.email}}
      </p>
  </div>

</div>
</template>

<script>
export default {
  data() {
    return {
      user: {},
    };
  },
  methods: {
    getUserDetails() {
        let user = localStorage.getItem('user');
        let token = localStorage.getItem('jwt');

        if (token){
            this.user = JSON.parse(user);
        }
    },
    logOut(){
        localStorage.removeItem('jwt');
        localStorage.removeItem('user');
        this.$router.push('/');
    },
  },
  created(){
      this.getUserDetails();
  }
};
</script>