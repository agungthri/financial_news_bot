import news_source as ns
from telegram_bot import sendMassage
import datetime
import aiohttp

async def main():
    
    async with aiohttp.ClientSession() as session:
        
        get_data_bisnis_data   = await ns.get_data_bisnis(session)
        get_data_cnbc_data     = await ns.get_data_cnbc(session)
        get_data_investor_data = await ns.get_data_investor(session)
        get_data_katadata_data = await ns.get_data_katadata(session)
        get_data_kontan_data   = await ns.get_data_kontan(session)
        get_data_kompas_data   = await ns.get_data_kompas(session)
        get_data_emiten_data   = await ns.get_data_emiten(session)

        while 1:

            for i in await ns.get_data_bisnis(session):
                if i in get_data_bisnis_data:
                    pass
                else:
                    get_data_bisnis_data.append(i)
                    await sendMassage("\n".join(i), session)
                    await ns.add_sleep()


            for i in await ns.get_data_cnbc(session):
                if i in get_data_cnbc_data:
                    pass
                else:
                    get_data_cnbc_data.append(i)
                    await sendMassage("\n".join(i), session)
                    await ns.add_sleep()


            for i in await ns.get_data_investor(session):
                if i in get_data_investor_data:
                    pass
                else:
                    get_data_investor_data.append(i)
                    await sendMassage("\n".join(i), session)
                    await ns.add_sleep()


            for i in await ns.get_data_katadata(session):
                if i in get_data_katadata_data:
                    pass
                else:
                    get_data_katadata_data.append(i)
                    await sendMassage("\n".join(i), session)
                    await ns.add_sleep()


            for i in await ns.get_data_kontan(session):
                if i in get_data_kontan_data:
                    pass
                else:
                    get_data_kontan_data.append(i)
                    await sendMassage("\n".join(i), session)
                    await ns.add_sleep()
                    
                    
            for i in await ns.get_data_kompas(session):
                if i in get_data_kompas_data:
                    pass
                else:
                    get_data_kompas_data.append(i)
                    await sendMassage("\n".join(i), session)
                    await ns.add_sleep()
                    
            for i in await ns.get_data_emiten(session):
                if i in get_data_emiten_data:
                    pass
                else:
                    get_data_emiten_data.append(i)
                    await sendMassage("\n".join(i), session)
                    await ns.add_sleep()

            print(datetime.datetime.now())
