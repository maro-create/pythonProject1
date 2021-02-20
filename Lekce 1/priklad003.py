volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}
hour = int(input("Zadejte číslo hodiny, kdy chcete zamluvit meeting room"))
if hour in volnePokoje:
  print(f"Pocet volnych mistnosti k dispozici je {len(volnePokoje[hour])}.")
else:
  print("V teto hodine bohuzel neni volna zadna meeting room.")