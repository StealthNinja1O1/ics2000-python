from typing import Optional
import logging

class Device:
    def __init__(self, name, entity_id, hb):
        self._hub = hb
        self._name = name
        self._id = entity_id
        logging.info(f'{str(self._name)} : {str(self._id)}')

    @property
    def id(self) -> int:
        return self._id

    @property
    def hub(self):
        return self._hub

    @property
    def name(self) -> str:
        return self._name

    def turn_off(self):
        cmd = self._hub.getcmdswitch(self._id, False)
        self._hub.send_command(cmd.getcommand())

    def turn_on(self):
        cmd = self._hub.getcmdswitch(self._id, True)
        self._hub.send_command(cmd.getcommand())

    def get_status(self) -> Optional[bool]:
        return self._hub.get_lamp_status(self._id)


class Dimmer(Device):
    def dim(self, level):
        if level < 0 or level > 15:
            return
        cmd = super()._hub.getcmddim(super()._hub, level)
        super()._hub.send_command(cmd.getcommand())


class Zigbee_Lamp:
    def __init__(self, name, entity_id, hb):
        self._hub = hb
        self._name = name
        self._id = entity_id
        logging.info(f'{str(self._name)} : {str(self._id)}')

    @property
    def id(self) -> int:
        return self._id

    @property
    def hub(self):
        return self._hub

    @property
    def name(self) -> str:
        return self._name

    def turn_off(self):
        cmd = super()._hub.getcmdswitch(super()._hub, False)
        super()._hub.send_command(cmd.getcommand())

    def turn_on(self):
        cmd = super()._hub.getcmdswitch(super()._hub, True)
        super()._hub.send_command(cmd.getcommand())

    def get_status(self) -> Optional[bool]:
        return self._hub.get_lamp_status(self._id)

    def dim(self, level):
        if level < 0 or level > 255:
            return
        cmd = super()._hub.getcmddim(super()._hub, level)
        super()._hub.send_command(cmd.getcommand())

    def color_temp(self, color_temp):
        if color_temp < 0 or color_temp > 600:
            return
        self._attr_color_temp = color_temp
        cmd = super()._hub.getcmdct(super()._hub, color_temp)
        super()._hub.send_command(cmd.getcommand()) 

    def toggle (self):
        cmd = super()._hub.getcmdtoggle(super()._hub)
        super()._hub.send_command(cmd.getcommand())

class Sunshade:
    def __init__(self, name, entity_id, hb):
        self._hub = hb
        self._name = name
        self._id = entity_id
        logging.info(f'{str(self._name)} : {str(self._id)}')

    @property
    def id(self) -> int:
        return self._id

    @property
    def hub(self):
        return self._hub

    @property
    def name(self) -> str:
        return self._name

    def open(self):
        cmd = super()._hub.getcmdsun(super()._hub, True)
        super()._hub.send_command(cmd.getcommand())

    def close(self):
        cmd = super()._hub.getcmdsun(super()._hub, False)
        super()._hub.send_command(cmd.getcommand())

    def stop(self):
        cmd = super()._hub.getcmdsun(super()._hub, None)
        super()._hub.send_command(cmd.getcommand())

    def get_status(self) -> Optional[bool]:
        return self._hub.get_lamp_status(self._id)