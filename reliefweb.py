contributions = {}
new_sheet = []

def to_int(num_as_str):
  return int(num.replace(',', ''))

for row in rows[10:]:
  contributions[row[d]] = {
    'Original Requirements (USD)': to_int(row[i]);
    'Revised requirements (USD)': to_int(row[k]);
    'Carry-over (USD)': to_int(row[m]);
    'Funding (USD)': to_int(row[q]);
    'Total resources available (USD)': to_int(row[t]);
    'Unmet requirements':to_int(row[aa]);
    '% Covered': row[af];
    'Uncommitted pledges': row[ak] or 0;
  }
  try contributions['Grand Total:']:
    break
  except KeyError:
    pass

new_sheet[0] = [label for label, figure in contributions['Grand Total:']]

for cluster in contributions:
  new_sheet.append(
    cluster['Original Requirements (USD)'],
    cluster['Revised requirements (USD)'],
    cluster['Carry-over (USD)'],
    cluster['Funding (USD)'],
    cluster['Total resources available (USD)'],
    cluster['Unmet requirements'],
    cluster['% Covered'],
    cluster['Uncommitted pledges'])

