defmodule RpiSunrise.Alarm do
  use GenServer

  def start_link do
    GenServer.start_link(__MODULE__, %{})
  end

  def init(state) do
    reset
    set_timer
    {:ok, state}
  end

  def handle_info(:check_alarms, state) do
    alarm = {05, 30}
    {_, {curr_hour, curr_minute, _}} = :calendar.local_time()

    if {curr_hour, curr_minute} == alarm, do: sunrise

    set_timer
    {:noreply, state}
  end

  defp set_timer do
    Process.send_after(self(), :check_alarms, 60 * 1000)
  end

  defp sunrise do
    System.cmd("sudo", ["python", "/home/pi/rpi_ws281x/python/examples/sunrise.py"])
  end

  defp reset do
    System.cmd("sudo", ["python", "/home/pi/rpi_ws281x/python/examples/reset.py"])
  end
end
