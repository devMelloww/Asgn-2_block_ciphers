import matplotlib.pyplot as plt

# Setting the dark theme
plt.style.use('dark_background')

def AES_plot():
    blockSizes = [16, 64, 256, 1024, 8192, 16384]
    throughput_128 = [324767.25,  333484.11, 335223.71, 331903.95, 349188.23, 354513.85]
    throughput_192 = [290960.05, 299528.17, 301921.84, 299044.74, 320793.30, 315214.84]
    throughput_256 = [262045.93, 250578.21, 264156.73, 241251.63, 236694.31, 241771.59]

    plt.figure(figsize=(10, 6))
    plt.plot(blockSizes, throughput_128, label='AES-128-CBC', marker='X')
    plt.plot(blockSizes, throughput_192, label='AES-192-CBC', marker='X')
    plt.plot(blockSizes, throughput_256, label='AES-256-CBC', marker='X')

    plt.title('Block Size vs. AES Throughput (for various key sizes)')
    plt.xlabel('Block Size (bytes)')
    plt.ylabel('Throughput (kB/s)')
    plt.legend()
    plt.grid(True)
    plt.savefig("../resources/plots/aes_throughput.png")

def RSA_plot():
    key_sizes = ['1024 bits', '2048 bits', '4096 bits']
    sign_per_second = [14296.4, 2225.4, 338.0]
    verify_per_second = [171414.2, 69370.3, 20261.7]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar([x for x in range(len(key_sizes))], sign_per_second, color='r', width=0.4, label='Sign/s')
    ax.bar([x + 0.4 for x in range(len(key_sizes))], verify_per_second, color='b', width=0.4, label='Verify/s')

    ax.set_xlabel('RSA Key Size')
    ax.set_ylabel('Operations per Second')
    ax.set_title('RSA Key Size vs. RSA Throughput')
    ax.set_xticks([x + 0.2 for x in range(len(key_sizes))])
    ax.set_xticklabels(key_sizes)
    ax.legend()
    plt.grid(True)
    plt.savefig("../resources/plots/rsa_throughput.png")

if __name__ == "__main__":
    AES_plot()
    RSA_plot()
