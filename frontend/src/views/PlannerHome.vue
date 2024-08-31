<template>
    <div class="container p-4">
        <!-- Top bar -->
        <div class="row justify-content-between">
            <div class="col-auto">
                <h1>Your Events</h1>
            </div>

            <div class="col-auto">
                <button class="btn btn-primary bg-orange">
                    <font-awesome-icon icon="fa-solid fa-plus" /> Add Event
                </button>
            </div>
        </div>

        <!-- Events -->
         <div class="row">
            <div class="col-12 bg-white mt-4 rounded" v-for="e_event in events">
                {{ e_event.title }}
            </div>
        </div>
    </div>
</template>


<script>
    export default {
        name: 'PlannerHome',
        data() {
            return {
                events: [
                    {
                        location: "amk",
                        title: "this is a test",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test 2",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test 3",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test 2",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test 3",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test 2",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test 3",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test 2",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test 3",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test 2",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test 3",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test 2",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                    {
                        location: "amk",
                        title: "this is a test 3",
                        description: "heheh",
                        planner_username : "planner2",
                        datetime: "2021-10-10 10:00:00",
                        num_participants: 10,
                    },
                ]
            }
        },
        methods: {
            fetchEvents() {
                // Fetch events from the API
            }
        },
    }
</script>


<style scoped>
    .bg-orange {
        background-color: #FB923C;
        border-color: #FB923C;
    }
    .bg-orange:hover {
        background-color: #be6923;
        border-color: #be6923;
    }
</style>