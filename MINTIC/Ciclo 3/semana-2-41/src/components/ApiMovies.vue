<template>
    <div class="row justify-content-center">
      <div
        class="col-sm-6 col-xs-12 col-lg-4" v-for="(movie, index) of movies" :key="index">
        <div class="card">
          <div class="d-flex justify-content-center">
            <img :src="movie.Poster" alt="movie poster" />
          </div>
          <div class="card-body">
            <div class="card-title">
              <h3>{{ movie.Title }}</h3>
              <hr />
              <h5>Descripción en inglés...</h5>
              <p>{{getPlot(index)}}</p>
            </div>
            <div class="d-flex container-fluid justify-content-end pb-2 mt-n2">
              <a
                :href="'https://www.imdb.com/title/' + movie.imdbID"
                target="_blank"
                class="btn btn-outline-info"
                >Info</a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ApiMovies",
  data() {
    return {
      movies: null,
      plots: [
        "A reluctant Hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home, and the gold within it from the dragon Smaug.",
        "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring.",
        "Bilbo and company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness.",
      ]
    };
  },
  mounted() {
    axios
      .get("http://www.omdbapi.com/?s=hobbit&type=movie&apikey=23daade9")
      .then((response) => {
        this.movies = response.data.Search.slice(0, 3);
        console.log(this.movies);
      });
  },
  methods: {
    getPlot(index){
      return this.plots[index];
    }
  }
};
</script>

<style scoped>
</style>