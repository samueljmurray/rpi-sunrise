defmodule RpiSunrice.NeopixelsService do
  
  def trigger_alarms do
    System.cmd("touch", ["~/hello.txt"])
  end

end