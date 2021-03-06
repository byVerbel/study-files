<template>
  <div id="app">
    <top-banner id="start"></top-banner>

    <div class="container-fluid mt-md-4" id="movies">
      <h1 class="d-flex justify-content-center">Películas</h1>
      <api-movies></api-movies>
    </div>

    <div class="container-fluid mt-md-4" id="animes">
      <h1 class="d-flex justify-content-center">Animes</h1>
      <api-anime></api-anime>
    </div>

    <div class="container-fluid mt-md-4" id="team">
      <h1 class="d-flex justify-content-center">Equipo</h1>
      <div class="row justify-content-center mb-5">
        <div class="col" v-for="(item, index) of team" :key="index">
          <team-card v-bind:member="item"></team-card>
        </div>
      </div>
    </div>

    <Footer></Footer>
  </div>
</template>

<script>
import Footer from "./components/Footer.vue";
import TopBanner from "./components/TopBanner.vue";
import TeamCard from "./components/TeamCard.vue";
import ApiMovies from "./components/ApiMovies.vue";
import ApiAnime from "./components/ApiAnime.vue";

export default {
  name: "App",
  components: {
    TopBanner,
    Footer,
    TeamCard,
    ApiMovies,
    ApiAnime,
  },
  
  data() {
    return {
      team: [
        {
          codigo: 1020818987,
          nombre: "Lucia Maria Ovalle M.",
          descripcion:
            "Profesion: Ing. Biomedica. Edad 24 Años. Pasatiempo Cocinar",
          rol: "Desarrolladora Backend",
          image: "./img/img_lucia.PNG",
        },
        {
          codigo: 9862724,
          nombre: "Jose A. Rodriguez B.",
          descripcion:
            "Profesion: Ing. Telecomunicaciones. Edad 34 Años. Pasatiempo Series",
          rol: "Desarrollador Backend",
          image: "./img/img_jose.PNG",
        },
        {
          codigo: 79420810,
          nombre: "Rosembel Suarez.",
          descripcion:
            "Profesion: Economista. Edad 40 Años. Pasatiempo Ajedrez",
          rol: "Desarrollador Backend",
          image: "./img/img_rosembel.PNG",
        },
        {
          codigo: 1152469687,
          nombre: "Sergio Luiz Lopez.",
          descripcion:
            "Profesion: Estudiante UNAL. Edad 21 Años. Pasatiempo Peliculas",
          rol: "Desarrollador Backend",
          image: "./img/img_sergio.PNG",
        },
      ],
    };
  },
};
</script>

