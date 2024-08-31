<script setup>
import { ref } from "vue";
import Scrollbar from "@/components/Scrollbar.vue";

const expandedIndex = ref(null);
const heartAnimated = ref(Array(10).fill(false));
const liked = ref(Array(10).fill(false));
const buttonText = ref(Array(10).fill("Join the fun"));

function toggleDetails(index) {
    expandedIndex.value = expandedIndex.value === index ? null : index;
}

function animateHeart(index) {
    if (!liked.value[index]) {
        heartAnimated.value[index] = true;

        setTimeout(() => {
            heartAnimated.value[index] = false;
            liked.value[index] = true;
        }, 800);
    } else {
        heartAnimated.value[index] = false;
        liked.value[index] = false;
    }
}

function handleButtonClick(index) {
    if (!liked.value[index]) {
        heartAnimated.value[index] = true;
        buttonText.value[index] = "Interest confirmed";

        setTimeout(() => {
            heartAnimated.value[index] = false;
            liked.value[index] = true;
        }, 800);
    } else {
        liked.value[index] = false;
        buttonText.value[index] = "Join the fun";
    }
}
</script>

<template>
    <main>
        <div class="welcome-container">
            <div class="profile-picture"></div>
            <div class="welcome-message">Hi, John Doe!</div>
            <div class="col-auto">
                <RouterLink
                    to="/login"
                    class="btn btn-primary bg-orange"
                    style="margin-left: 10px"
                >
                    Log out
                </RouterLink>
            </div>
        </div>

        <div class="event-container">
            <div class="event-container-title">Upcoming Events</div>
            <Scrollbar>
                <div class="" v-for="n in 10" :key="n">
                    <div
                        class="card event-card"
                        style="width: 20rem; margin-bottom: 20px"
                    >
                        <img
                            src="/event-aid-logo.png"
                            class="card-img-top"
                            alt="..."
                        />
                        <div class="card-body">
                            <h5 class="card-title">Tai Chi Session</h5>
                            <p class="card-text">5 Sep 2024</p>
                            <p class="d-inline-flex gap-1">
                                <button
                                    class="btn btn-color"
                                    type="button"
                                    data-bs-toggle="collapse"
                                    :data-bs-target="'#collapseExample' + n"
                                    aria-expanded="false"
                                    :aria-controls="'collapseExample' + n"
                                    @click="toggleDetails(n)"
                                >
                                    {{
                                        expandedIndex === n
                                            ? "x"
                                            : "Click for more details"
                                    }}
                                </button>
                            </p>
                            <div class="collapse" :id="'collapseExample' + n">
                                <div class="card card-body">
                                    <div
                                        class="event-description"
                                        style="margin-bottom: 10px"
                                    >
                                        Lorem ipsum dolor sit amet consectetur
                                        adipisicing elit. Atque necessitatibus
                                        ab minus facilis iure. Minima iste
                                        eligendi officia unde esse.
                                    </div>
                                    <div
                                        class="event-location"
                                        style="margin-bottom: 10px"
                                    >
                                        Bukit Batok Community Center
                                    </div>
                                    <div class="btn-event-container">
                                        <button
                                            class="btn event-indicate"
                                            @click="handleButtonClick(n - 1)"
                                        >
                                            {{ buttonText[n - 1] }}
                                        </button>
                                        <div
                                            class="event-heart-icon"
                                            :class="{
                                                animate: heartAnimated[n - 1],
                                                liked: liked[n - 1],
                                            }"
                                        ></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </Scrollbar>
        </div>
    </main>
</template>

<style scoped>
.welcome-container {
    margin: 20px 0 0 30px;
    color: black;
    align-items: center;
    display: flex;
    flex-direction: row;
}

.profile-picture {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: 1px solid black;
}

.welcome-message {
    margin-left: 10px;
}

.event-container {
    margin: 20px 0 0 30px;
    color: black;
    align-items: center;
}

.event-container-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}

.btn {
    background-color: #ff7300;
    color: #ffffff;
    font-size: 13px;
    letter-spacing: 0.04em;
}

.event-description,
.event-location {
    font-size: 13px;
    letter-spacing: 0.04em;
}

.btn-event-container {
    display: flex;
    flex-direction: row;
}

.event-heart-icon {
    background-image: url("https://s3-us-west-2.amazonaws.com/s.cdpn.io/66955/web_heart_animation.png");
    background-repeat: no-repeat;
    background-size: 2900%;
    background-position: left;
    height: 50px;
    width: 50px;
    cursor: pointer;
}

.liked {
    background-position: right;
}

.animate {
    animation: heart-burst 0.8s steps(28) forwards;
}
@keyframes heart-burst {
    0% {
        background-position: left;
    }
    100% {
        background-position: right;
    }
}

.card-img-top {
    width: 100%;
    height: 15vw;
    object-fit: cover;
}

.col-auto {
    margin-left: auto;
    margin-right: 1rem;
}
</style>
