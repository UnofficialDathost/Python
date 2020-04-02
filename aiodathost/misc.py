class Misc(object):
    async def account(self):
        """ Returns account infomation. """

        return await self._get(url=self.routes["account"])

    async def domains(self):
        """ Returns Dathost's domains. """

        return await self._get(url=self.routes["domains"])