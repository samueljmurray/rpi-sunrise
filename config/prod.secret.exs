use Mix.Config

# In this file, we keep production configuration that
# you likely want to automate and keep it away from
# your version control system.
config :rpi_sunrise, RpiSunrise.Endpoint,
  secret_key_base: "kqXSJ91Fu8YanXZdKQpp4W/8vxC+qIrNbHKi9o0+x4RyqoczLI7v9X65ydrROCA1"

# Configure your database
config :rpi_sunrise, RpiSunrise.Repo,
  adapter: Ecto.Adapters.Postgres,
  username: "postgres",
  password: "postgres",
  database: "rpi_sunrise_prod",
  pool_size: 20
