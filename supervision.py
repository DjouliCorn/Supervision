"""Supervision

Copyright (c) 2021 Julie Tissier
This program take the info about the CPU, the memory, disk C, disk D and the network traffic.
It writes the information inside a text file (info.text), a database (supervision).

"""
import time

import mariadb
import psutil

space = "\n"


def get_net_io_counters():
    """Get the net I/O counters
    :return: informations about ethernet connection or wifi
    """

    return psutil.net_io_counters(
        pernic=True,
        nowrap=False,
    )


def net_io_counters_gestion():
    """ THE NETWORK
                     - name of the network
                     - bytes sent
                     - bytes received
                     - packets sent
                     - packets received  """
    counters = get_net_io_counters()

    title = "Network info => "
    write_into_file(title)

    for data in counters:
        #
        # Get info from the function get_net_io_counters and extract them in a loop
        #
        network_name = data
        bytes_sent = counters[data][0]
        bytes_recv = counters[data][1]
        packets_sent = counters[data][2]
        packets_recv = counters[data][3]
        #
        # Join all the info to write them in the info.txt, add some titles for the presentation
        #
        network_info_temporary = "".join(
            network_name + " : " + "bytes_sent : " + str(bytes_sent) + " / bytes_received : " + str(bytes_recv)
            + " / packets_sent : " + str(packets_sent) + " / packets_recv : " + str(packets_recv)
        )

        file_text = f"{network_info_temporary}"
        write_into_file(file_text)
        #
        # Creation of the query to insert the info into the database,
        # also inside the loop to have all informations from all the networks of the computer
        #
        sqlstatement_network = f"INSERT INTO net_io_counter" \
                               f"(" \
                               f"name, bytes_sent, bytes_recv, packets_sent, packets_recv" \
                               f") " \
                               f"VALUES (" \
                               f"'{network_name}'," \
                               f" '{bytes_sent}', " \
                               f" '{bytes_recv}', " \
                               f" '{packets_sent}', " \
                               f" '{packets_recv}') "
        write_to_db(sqlstatement_network)


def get_cpu_info():
    """Get cpu info
    :return: percent of usage of the cpu
    """
    return psutil.cpu_percent(
        interval=None,
        percpu=False
    )


def cpu_info_gestion():
    cpu_percent = round(get_cpu_info())
    file_text = f"CPU => {cpu_percent} %"
    write_into_file(file_text + space)
    #
    # Query to insert the infos about the cpu in the database
    #
    sqlstatement_cpu = f"INSERT INTO cpu_usage" \
                       f"(" \
                       f"cpu_percent" \
                       f") " \
                       f"VALUES (" \
                       f"'{cpu_percent}')"
    write_to_db(sqlstatement_cpu)


def get_memory():
    """Get the informations about the memory
    :returns: the virtual memory stats
    """
    return psutil.virtual_memory()


def memory_gestion():
    """THE MEMORY
        - total
        - available
        - percent
        - used
        - free"""
    #
    # Get the info from the psutil
    #
    memory_info = get_memory()
    memory_stats = [
        "Total : " + str(memory_info.total),
        " / Available : " + str(memory_info.available),
        " / Percent : " + str(memory_info.percent),
        " / Used : " + str(memory_info.used),
        " / Free : " + str(memory_info.free),
    ]
    #
    # Join the info to write them in the info.txt
    #
    memory_stats_towrite = "".join(memory_stats)

    file_text = f"Memory => {memory_stats_towrite}"
    write_into_file(space + file_text + space)
    #
    # Insert info into the database
    #
    sqlstatement_memory = f"INSERT INTO memory" \
                          f"(" \
                          f"total, available, percent, used, free" \
                          f") " \
                          f"VALUES (" \
                          f"'{memory_info.total}'," \
                          f" '{memory_info.available}', " \
                          f" '{round(memory_info.percent)}', " \
                          f" '{memory_info.used}', " \
                          f" '{memory_info.free}') "
    write_to_db(sqlstatement_memory)


def get_disk_usage(direction):
    """Get the information about the disk link in the path
    :param: the direction of the disk

    :return: the information of the disk
    """

    return psutil.disk_usage(direction)


def disk_usage_c_gestion():
    """Info about the spaces on the disk c
         - Total
         - Used
         - Free
         - Percent"""
    #
    # Take the info about the disk C from the function psutil
    #
    disk_info_c = get_disk_usage('C:')
    disk_stats_c = [
        "Total space: " + str(disk_info_c.total),
        " - Used space: " + str(disk_info_c.used),
        " - Free space : " + str(disk_info_c.free),
        " - Percent : " + str(disk_info_c.percent),
    ]
    disk_info_c_towrite = "".join(disk_stats_c)
    #
    # Write the info into the info.txt
    #
    file_text_c = f"Disk C =>  {disk_info_c_towrite} %"
    write_into_file(file_text_c)
    #
    # Insert info about the disk C into the database
    #
    sqlstatement_disk_c = f"INSERT INTO disk_usage_c" \
                          f"(" \
                          f"total, used, free, percent" \
                          f") " \
                          f"VALUES (" \
                          f"'{disk_info_c.total}'," \
                          f" '{disk_info_c.used}', " \
                          f" '{disk_info_c.free}', " \
                          f" '{round(disk_info_c.percent)}') "
    write_to_db(sqlstatement_disk_c)


def disk_usage_d_gestion():
    """Info about the spaces on the disk d
             - Total
             - Used
             - Free
             - Percent"""
    #
    # Take the info about the disk D from the function psutil
    #
    disk_info_d = get_disk_usage('D:')
    disk_stats_d = [
        "Total space: " + str(disk_info_d.total),
        " / Used space: " + str(disk_info_d.used),
        " / Free space : " + str(disk_info_d.free),
        " / Percent : " + str(disk_info_d.percent),
    ]
    disk_info_d_towrite = "".join(disk_stats_d)
    #
    # Write the info into the info.txt
    #
    file_text_d = f"Disk D =>  {disk_info_d_towrite} %"
    write_into_file(file_text_d + space)

    #
    # Insert info about the disk D into the database
    #
    sqlstatement_disk_d = f"INSERT INTO disk_usage_d" \
                          f"(" \
                          f"total, used, free, percent" \
                          f") " \
                          f"VALUES (" \
                          f"'{disk_info_d.total}'," \
                          f" '{disk_info_d.used}', " \
                          f" '{disk_info_d.free}', " \
                          f" '{round(disk_info_d.percent)}') "
    write_to_db(sqlstatement_disk_d)


def write_into_file(text):
    """
    Write informations into a text file (string only)
    :param text: the informations grab by the psutil call
    """
    with open("info.txt", "a+") as file:
        file.write(text + "\n")


def write_to_db(sqlstatement):
    """Write to mySQL
    """
    try:
        conn = mariadb.connect(
            user="root",
            password="root",
            host="127.0.0.1",
            port=3306,
            database="supervision"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MySQL Platform: {e}")
        return
    cur = conn.cursor()
    cur.execute(sqlstatement)
    conn.commit()
    conn.close()


def main():
    """The main function"""

    while True:
        try:
            time.sleep(10)

            """ THE CPU """

            cpu_info_gestion()

            """ THE NETWORK"""

            net_io_counters_gestion()

            """THE MEMORY"""

            memory_gestion()

            """The disk C and D"""

            disk_usage_c_gestion()
            disk_usage_d_gestion()

        except KeyboardInterrupt:

            break


if __name__ == '__main__':
    main()
