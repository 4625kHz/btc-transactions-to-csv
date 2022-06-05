###############################################################################
### READS TRANSACTION HISTORY OF A BTC ADDRESS AND OUTPUTS DATA TO CSV FILE ###
###############################################################################

# Import modules
import urllib.request, json, csv
import datetime

# Read JSON file from blockchain
btc_addr = "1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
web_addr = "https://blockchain.info/rawaddr/" + btc_addr + "?limit=10000"

with urllib.request.urlopen(web_addr) as url:
	data = json.loads(url.read().decode())

# Print analysis summary
print ("BTC Address: " + btc_addr)
print ("Current Balance: " + str(data['final_balance'] / 100000000) + " BTC")
print ("Total Transactions: " + str(data['n_tx']))

# Create output file header
header = ['Date/Time', 'Amount (BTC)']

# Set transaction counters
count = len(data['txs'])
tx_count = 0

# Set transaction size threshold
tx_threshold = 50000000

# Create CSV output file
with open('data_file_5.csv', 'w') as output:
	writer = csv.writer(output)

	# write header row to CSV file
	writer.writerow(header)

	# Write data
	for x in data['txs']:

		# Transactions greater than 0.5 BTC only
		if abs(data['txs'][count-1]['result']) > tx_threshold:
			dt_obj = datetime.date.fromtimestamp(data['txs'][count-1]['time'])
			btc_amt = data['txs'][count-1]['result'] / 100000000

			row_val = [dt_obj, btc_amt]
			writer.writerow(row_val)

			tx_count += 1

		count = count - 1

output.close()

# Final output summary
print ("Transaction Threshold: " + str(tx_threshold / 100000000) + " BTC")
print ("Output Transactions: " + str(tx_count))
print ("Output Complete")
print (" ")
