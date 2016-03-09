defmodule RpiSunrise.PageController do
  use RpiSunrise.Web, :controller

  def index(conn, _params) do
    render conn, "index.html"
  end
end
