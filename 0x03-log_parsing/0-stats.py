from collections import defaultdict


def is_valid_line(line):
    """Checks if the line follows the expected format."""
  try:
      # Split the line based on spaces
    parts = line.split()
    # Check if all expected parts exist
    return len(parts) == 7 and parts[0].count(".") == 3 and int(parts[4]) and int(parts[6])
  except ValueError:
    return False


def process_line(line, stats):
    """Processes a valid line and updates statistics."""
    status_code = int(line.split()[4])
    file_size = int(line.split()[6])
    stats["total_size"] += file_size
    stats["status_codes"][status_code] += 1


def print_stats(stats):
    """Prints the current statistics."""
    print(f"Total file size: {stats['total_size']}")
    print("Number of lines by status code:")
  for code, count in sorted(stats["status_codes"].items()):
      print(f"{code}: {count}")


def main():
    """Main function that reads lines and prints statistics."""
    stats = {"total_size": 0, "status_codes": defaultdict(int)}
    line_count = 0
  try:
    for line in sys.stdin:
        line = line.rstrip()  # Remove trailing newline
      if is_valid_line(line):
          process_line(line, stats)
          line_count += 1
        if line_count % 10 == 0:
            print_stats(stats)
            stats = {"total_size": 0, "status_codes": defaultdict(int)}
            line_count = 0
  except KeyboardInterrupt:
      print_stats(stats)
      print("\nInterrupted by user.")


if __name__ == "__main__":
    main()
