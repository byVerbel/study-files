<template>
  <nav class="navbar navbar-expand-lg sticky-top navbar-dark bg-info">
    <a class="navbar-brand mb-0 h1" href="# ">
      <img
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Yin_yang.svg/480px-Yin_yang.svg.png"
        width="30"
        height="30"
        class="d-inline-block align-top"
        alt=" "
        loading="lazy "
      />
      Grupo 41
    </a>
    <div
      class="collapse navbar-collapse justify-content-center"
      id="navbarNav "
    >
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" href="#start"
            >Inicio <span class="sr-only">(current)</span></a
          >
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#movies">Películas</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#animes">Animes</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#team">Equipo</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: "TopMenu",
};
</script>

<style scoped>
</style>