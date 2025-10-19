from linked_list import LinkedList

if __name__ == "__main__":
    onigiri_preparation = LinkedList()

    onigiri_preparation.insert_at_end("cook rice")
    onigiri_preparation.insert_at_end("season rice with salt")
    onigiri_preparation.insert_at_end("prepare filling (like tuna or salmon)")
    onigiri_preparation.insert_at_end("shape rice into triangle or ball")
    onigiri_preparation.insert_at_end("wrap with nori (seaweed)")
    onigiri_preparation.insert_at_beginning("wash rice")

    print("Onigiri Preparation Steps:")
    onigiri_preparation.display()

    print("\nRemoving first step...")
    removed = onigiri_preparation.remove_beginning()
    print(f"Removed: {removed}")
    onigiri_preparation.display()

    print("\nRemoving last step...")
    removed = onigiri_preparation.remove_at_end()
    print(f"Removed: {removed}")
    onigiri_preparation.display()

    print("\nRemoving 'prepare filling (like tuna or salmon)' step...")
    removed = onigiri_preparation.remove_at("prepare filling (like tuna or salmon)")
    print(f"Removed: {removed}")
    onigiri_preparation.display()
